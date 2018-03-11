function b() {
  // document.getElementById('b').setAttribute("class","column blue");
}
$(document).ready(function() {
$('.ui.dropdown')
  .dropdown()
;
$('.ui.form')
  .form({
    fields: {
      username: {
        identifier: 'username',
        rules: [
          {type   : 'empty', prompt : 'Please enter your username!'}
          // add checker to existing username here.
        ]
      },
      password: {
        identifier: 'password',
        rules: [
          {type   : 'empty', prompt : 'Please enter your password!'},
          {type   : 'regExp[/^[a-zA-Z0-9]{6,20}$/]', prompt : 'Your password should be 6-20 characters long with only digits or letters'}
        ]
      },
      
    }
  })
;
})
