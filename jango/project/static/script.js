
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
            return true;
        }