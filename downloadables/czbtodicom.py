import numpy as np
import sys
import io
import pydicom
from pydicom._uid_dict import UID_dictionary
from pydicom.dataset import Dataset, FileDataset
import datetime, time
import struct
import pickle

""" PYTHON SCRIPT TO CONVERT CZB FILE TO DICOM FILE """

def writedicom():
    new_file=open('CT-MONO2-16-brain.czb','rb') #SPECIFY THE INPUT FILENAME

    content=new_file.read()

    filename='CT-MONO2-16-brainv4.dcm'  #SPECIFY THE OUTPUT FILE NAME

    new_file.seek(17)
    r=new_file.read(8)
    rows=struct.unpack('Q',r)[0]
    new_file.seek(25)
    c=new_file.read(8)
    columns=struct.unpack('Q',c)[0]
    new_file.seek(33)
    b=new_file.read(1)
    bpp=struct.unpack('B',b)[0]
    new_file.seek(34)
    pixeldata = new_file.read()
    pdata=np.array(pixeldata,dtype=np.uint8)
    #pdata.reshape(w,h)

    #ADDITIONAL DATA REQUIRED IN DICOM FILENAME

    file_meta = Dataset()
    file_meta.MediaStorageSOPClassUID = 'Secondary Capture Image Storage'
    file_meta.MediaStorageSOPInstanceUID = '1.3.6.1.4.1.9590.100.1.1.111165684411017669021768385720736873780'
    file_meta.ImplementationClassUID = '1.3.6.1.4.1.9590.100.1.0.100.4.0'
    ds = FileDataset(filename, {},file_meta = file_meta,preamble="\0"*128)
    ds.Modality = 'CT'
    ds.ContentDate = str(datetime.date.today()).replace('-','')
    ds.ContentTime = str(time.time()) #milliseconds since the epoch
    ds.StudyInstanceUID =  '1.3.6.1.4.1.9590.100.1.1.124313977412360175234271287472804872093'
    ds.SeriesInstanceUID = '1.3.6.1.4.1.9590.100.1.1.369231118011061003403421859172643143649'
    ds.SOPInstanceUID =    '1.3.6.1.4.1.9590.100.1.1.111165684411017669021768385720736873780'
    ds.SOPClassUID = 'Secondary Capture Image Storage'
    ds.SecondaryCaptureDeviceManufctur = 'Python 2.7.3'
    ds.SamplesPerPixel = 1
    ds.PhotometricInterpretation = "MONOCHROME2"
    ds.PixelRepresentation = 1
    ds.HighBit = 15
    ds.BitsStored = 16
    ds.WindowCenter = 50
    ds.WindowWidth = 75
    ds.BitsAllocated=bpp
    ds.Rows=rows
    ds.Columns=columns
    ds.PixelData = pdata
    print ds.PixelData
    ds.save_as(filename) #DICOM FILE IS SAVED IN THE DIRECTORY WITH THE GIVEN FILE NAME
    return "filesaved"

def main():
    writedicom()

if __name__=='__main__':
    main()
