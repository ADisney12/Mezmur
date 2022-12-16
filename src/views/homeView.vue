<script>
  import axios from 'axios';
  export default{
    data(){
      let username = this.$route.params.name;
      let password = this.$route.params.password;
      return{
        input: "",
        vid: null,
        signInVar: null,
        Createusername: "",
        Createpassword: "",
        invalid: null,
        username: "",
        password: "",
        invalidUser: null,
        username,
        password

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

  
    }
  }
</script>


<template>
   <div class="sidenav" >
    <h1 id = "title">Mezmur</h1>
    <a @click="GoToSearch()">search</a>
    <a @click="GoToPlaylists()">playists</a>
    <a>Songs</a>
    <a>artists</a>
    </div>
  <router-view>
    
  </router-view>
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
