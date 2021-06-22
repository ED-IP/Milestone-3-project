 $(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('input#username, textarea#term, textarea#definition').characterCounter();
  });