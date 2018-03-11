$(document).ready(function() {
$('.ui.dropdown')
  .dropdown()
;
$('.ui.form')
  .form({
    onSuccess: function(){
      $('.ui.column.hidden.success.message').attr("class", "ui column success message")
    },
    fields: {
      'email-address': {
        identifier: 'email-address',
        rules: [
          {type   : 'email', prompt : 'Not a valid Email Address!'}
        ]
      },
      password: {
        identifier: 'password',
        rules: [
          {type   : 'regExp[/^[a-zA-Z0-9]{6,20}$/]', prompt : 'Your password should be 6-20 characters long with only digits or letters'}
        ]
      },
      'confirm-password':{
        identifier: 'confirm-password',
        rules: [
          {type   : 'match[password]', prompt : 'You entered different password!'}
        ]
      },
      username: {
        identifier: 'username',
        rules: [
          {type   : 'regExp[/^(?![0-9]+$)(?=[a-zA-Z0-9-]{5,25}$)[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*$/]',
          prompt : "The username: <br>- will consist of only a-z, A-Z, 0-9 and - (hyphen)<br>- shall not consist of ONLY digits or ONLY hyphens but it can have only characters<br>- The first & last characters shouldn't be hyphens (it can be digits but not entirely digits)<br>- There shouldn't be 2 hyphens back to back<br>- Minimum number of chars is 5 and max is 25;"},
          // add checker to existing username here.
        ]
      },
      birthday: {
        identifier: 'birthday',
        optional: true,
        rules:[
          {type   : 'regExp[/^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/]', prompt : 'Not a valid birthday!'}
        ]
      }
    }
  })
;
})
