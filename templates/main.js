
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-app.js";
//   import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-analytics.js";
  import { getAuth,GoogleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-auth.js";

  const firebaseConfig = {
    apiKey: "AIzaSyAJClJfnz1gCDZaCA13iiOjjqgGxIuLjSc",
    authDomain: "login-f49d4.firebaseapp.com",
    projectId: "login-f49d4",
    storageBucket: "login-f49d4.appspot.com",
    messagingSenderId: "196931593691",
    appId: "1:196931593691:web:da6559b2d9cda70a8db3fe",
  };

  const app = initializeApp(firebaseConfig);
  const auth = getAuth(app);
  auth.languageCode ='en'
  const provider = new GoogleAuthProvider();

  const googleLogin = document.getElementById("google-login-btn");
  googleLogin.addEventListener("click",function(){

    signInWithPopup(auth, provider)
      .then((result) => {
        const credential = GoogleAuthProvider.credentialFromResult(result);
        const user = result.user;
        console.log(user);
        window.location.href="../logged.html";

      }).catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
      });
  })