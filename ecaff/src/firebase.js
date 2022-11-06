// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAF6iuHNXvcZ9-aG54PMKx8zdwOd5nzI3k",
  authDomain: "ecaff-367805.firebaseapp.com",
  projectId: "ecaff-367805",
  storageBucket: "ecaff-367805.appspot.com",
  messagingSenderId: "603463206679",
  appId: "1:603463206679:web:0fd35c535b926811735952",
  measurementId: "G-K2GH31E5X4"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

//export const database = getFirestore(app);
const database = getFirestore(app);
const storage = getStorage(app);
