<script>
  import axios from 'axios';
  export default{
    data(){

      return{
        input: "",
        vid: null,
        signInVar: null,
        Createusername: "",
        Createpassword: "",
        invalid: null,
        username: "",
        password: "",
        invalidUser: null

      }

    },
    mounted(){
      this.$route
      this.signInVar = false
      console.log(this.$router.currentRoute.path)

    },
    methods:{
      query(){
        console.log("sasd")
        const path = "http://127.0.0.1:5000/search/" + this.input
        axios.get(path)
        .then(res => {
        console.log(res.data.url)
        var audio = new Audio(res.data.url)
        audio.play()
      })
      },
      GoToSearch(){
        this.$router.push({ name: 'search', params: { name: this.username, password: this.password} })
        },
        GoToPlaylists(){
            this.$router.push({ name: 'playlists', params: { name: this.username, password: this.password} })
        },
      create(){
        axios.get("http://127.0.0.1:5000/Create/" + this.Createusername + "/" + this.Createpassword)
        .then(res => {
          console.log(res)
          if(res.data == "username already taken"){
            this.invalid = true
          }
          else{
            this.invalid = false
          }
        })
      },
      signIn(){
        axios.get("http://127.0.0.1:5000/SignIn/" + this.username + "/" + this.password)
        .then(res => {
          console.log(res.data)
          console.log(this.signInVar)
          if(res.data == "success"){
            console.log("yesss")
            this.$router.push({name: 'home', params: { name: this.username, password: this.password} })
            console.log(this.signInVar)
          }
          if(res.data == "invalid"){
            console.log("nooo")
            this.invalidUser = true
            console.log(this.signInVar)
          }
        })
      }

  
    }
  }
</script>


<template>

  <div>
      <div id="signIn">
      <h1>Sign in</h1>

        <input v-model = "username" type="text" placeholder="type your username">
        <p id = "username_message" v-if = "invalidUser">invalid password or username</p>
        <input v-model = "password" placeholder="type your password" id = "password" type="text">
        <button @click = "signIn()" id = "signInButton">Sign in</button>
    </div>
    <div id ="CreateAcount">
      <h1>create account</h1>
      <input  v-model = "Createusername" type="text" placeholder="type your username">
      <input v-model = "Createpassword" placeholder="type your password" id = "password" type="text">
      <button @click = "create()" id = "CreateAcountButton">create</button>
      <p id = "username_message" v-if = "invalid">username already taken</p>
      <p id = "username_made" v-if = "(invalid == false)">account has been created</p>
    </div>
  </div>
</template>

<style>
#CreateAcountButton{
  left: 1%;
  width: 90%;
  position: absolute;
  top: 150%;
}
#signInButton{
  left: 1%;
  width: 100%;
  position: absolute;
  top: 150%;
}
#CreateAcount{
  top: 40%;
  position: absolute;
  left: 50%;
  color: white;
}
#password{
  position: absolute;
  left: 1%;
  top: 100%;
}
#signIn{
  position: absolute;
  left: 50%;
  color: white;
}
#title{
  position: relative;
  left: 6%;
  color: rgb(197, 189, 189);
}
.sidenav {
  height: 100%; /* Full-height: remove this if you want "auto" height */
  width: 160px; /* Set the width of the sidebar */
  position: fixed; /* Fixed Sidebar (stay in place on scroll) */
  z-index: 1; /* Stay on top */
  top: 0; /* Stay at the top */
  left: 0;
  background-color: #111; /* Black */
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: 20px;
}

body{
  background-color: rgb(37, 35, 35);
}

/* The navigation menu links */
.sidenav a {
  padding: 6px 8px 6px 16px;
  text-decoration: none;
  font-size: 25px;
  color: #818181;
  display: block;
}

/* When you mouse over the navigation links, change their color */
.sidenav a:hover {
  color: #f1f1f1;
}

#search_icon{
  color: rgb(233, 223, 223);
  font-size: 200%;
  position: relative;
  left: 90%;
  border: 3px rgb(233, 223, 223);;
  width: 10%;
}
#search_icon:hover{
  color: #f1f1f1;
}

#username_message{
  color: red;
}
#username_made{
  color: greenyellow;
}
</style>
