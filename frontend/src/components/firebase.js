import firebase from 'firebase'
      // Initialize Firebase
	var config = {
		apiKey: "AIzaSyDj-Wlw5dHvRE_64dLqdGoy03EoSbOueGM",
		authDomain: "fir-chat-36131.firebaseapp.com",
		databaseURL: "https://fir-chat-36131.firebaseio.com",
		projectId: "fir-chat-36131",
		storageBucket: "",
		messagingSenderId: "473992336854"
	};
	firebase.initializeApp(config);
	export default firebase;