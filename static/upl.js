


function photo(){

  var pic=document.getElementByName('js-upload-files').files[0];

  var a='Date ::'+pic.date;
  a+='<br> Name ::'+pic.name;
  a+='<br> Size ::'+pic.size;
  a+='<br> Type ::'+pic.type;

  var filetype= 'application/*';

  if (!pic.type.match(filetype))
    {document.getElementById('res').innerHTML="invalid file format"}


  else{

    document.getElementById('res').innerHTML= a;


    }


}
