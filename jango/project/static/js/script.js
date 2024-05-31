//******************************* signup validation form  ***********************************

        function validateForm() {
            var name = document.getElementById("name").value;
            if(name.length >= 50){
                alert("Enter the name within 50 characters.")
                return false;
            }
            var phone = document.getElementById("phone").value;
            if (phone.length !== 10) {
                alert("Enter a 10-digit phone number.");
                return false;
            }
            var email = document.getElementById("email").value;
            if (!email.includes('@gmail.com')) {
                alert("Enter a valid email address.");
                return false;
            }
            var pass1 =document.getElementById("password1").value;
            var pass2 =document.getElementById("password2").value;
            if(pass1 !== pass2){
                alert("password didn't matched...")
                return false;
            }
            var pass1 =document.getElementById("password1").value;
            if(pass1.length < 8){
                alert("Password atleast 8 characters.")
                return false;
            }
            var pass1 =document.getElementById("password1").value;
            var passwordPattern = /^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$/;
            if (!passwordPattern.test(pass1)) {
                alert("Password must contain at least one letter and one number.");
                return false;
            } 
            return true;
        }

// *********************************** END *****************************************

// **********************************login form validation***************************

function loginform() {
    var email = document.getElementById('email').value;
    if (!email.includes('@gmail.com') ) {
        alert('Enter valid email address...')
        return false;
    }

    var pass1 =document.getElementById("password").value;
    var passwordPattern = /^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$/;
    if (!passwordPattern.test(pass1)) {
        alert("Password must contain at least one letter and one number.");
        return false;
    }

    var pass1 =document.getElementById("password").value;
    if(pass1.length && pass2.length < 8){
        alert("Password atleast 8 characters.")
        return false;
    }
    return true;
}