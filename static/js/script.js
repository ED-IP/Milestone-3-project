 $(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('textarea#term, textarea#definition').characterCounter();
  });