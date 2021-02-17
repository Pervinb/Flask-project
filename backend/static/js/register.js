function registration()
{

    var name= document.getElementById("firstName").value;
    var lastname= document.getElementById("lastName").value;
    var email= document.getElementById("email").value;
    var uname= document.getElementById("username").value;
    var pwd= document.getElementById("password").value;			
    var cpwd= document.getElementById("password2").value;
    var numb= document.getElementById("phone").value;
    
    //email id expression code
    var pwd_expression = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])/;
    var letters = /^[A-Za-z]+$/;
    var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    var numbers = /^\+?([0-9]{10})$/;

    if(name=='')
    {
        alert('Please enter your name');
    }
    else if(!letters.test(name))
    {
        alert('Name field required only alphabet characters');
    }
    if(lastname=='')
    {
        alert('Please enter your lastname');
    }
    else if(!letters.test(lastname))
    {
        alert('LastName field required only alphabet characters');
    }
    
    else if(uname=='')
    {
        alert('Please enter the user name.');
    }
    else if(!letters.test(uname))
    {
        alert('User name field required only  alphabet characters');
    }
    else if(numb=='')
    {
        alert('Please enter your number');
    }
    else if(!numbers.test(numb))
    {
        alert('Phone field required only 10 digit number  characters');
    }
    else if(email=='')
    {
        alert('Please enter your user email id');
    }
    else if (!filter.test(email))
    {
        alert('Invalid email');
    }
    else if(pwd=='')
    {
        alert('Please enter Password');
    }
    else if(cpwd=='')
    {
        alert('Enter Confirm Password');
    }
    else if(!pwd_expression.test(pwd))
    {
        alert ('Upper case, Lower case, Special character and Numeric letter are required in Password filed');
    }
    else if(pwd != cpwd)
    {
        alert ('Password not Matched');
    }
    else if(document.getElementById("password2").value.length < 6)
    {
        alert ('Password minimum length is 6');
    }
    else if(document.getElementById("password2").value.length > 12)
    {
        alert ('Password max length is 12');
    }
    else
    {				                            
           alert('Thank You for Registration');
           // Redirecting to other page or webste code. 
           window.location = "index.html"; 
    }
}