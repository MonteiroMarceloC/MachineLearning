from firebase import firebase
firebase = firebase.FirebaseApplication('https://buddysia-c2150.firebaseio.com/', None)
result = firebase.get('/test2', None)
print (result)
