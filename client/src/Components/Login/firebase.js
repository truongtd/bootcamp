import firebase from "firebase/compat/app"
import "firebase/compat/auth"

const firebaseConfig = {
    apiKey: "AIzaSyD08HmHLYdjq5een7igYAqPtBd1mDqGqtg",
    authDomain: "gomarket-896c3.firebaseapp.com",
    databaseURL: "https://gomarket-896c3.firebaseio.com",
    projectId: "gomarket-896c3",
    storageBucket: "gomarket-896c3.appspot.com",
    messagingSenderId: "721114980169",
    appId: "1:721114980169:web:cb3a15c3d9793169310498",
    measurementId: "G-GGKEGSX8BC"
  };
const app=firebase.initializeApp(firebaseConfig);
export const auth=app.firebase.auth();
export default app