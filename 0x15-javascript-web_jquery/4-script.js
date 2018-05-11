$("#toggle_header").click( function() {
  $( this ).toggleClass( "green red" );
});

$( "#toggle_header" ).toggleClass(function() {
    if ( $( this ).parent().is( ".red" ) ) {
      $( this ).removeClass( 'red' );
      return "green";
    } else {
      $( this ).removeClass( 'green' );
      return "red";
    }
});
