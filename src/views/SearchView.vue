<script>
import axios from 'axios';
export default {
    data(){
        let username = this.$route.params.name;
        let password = this.$route.params.password;
        return{
            username,
            password,
            input: "",
            results: "",
            resI: "",
            test: "",
            status: "pause",
            audio: new Audio(),
            num: 1,
            SongThatsPLaying: null

        }

    },
    mounted(){
      
    },
    methods:{
        queryList(){
            console.log("sasd")
            const path = "http://127.0.0.1:5000/searchList/" + this.input
            axios.get(path)
            .then(res => {
            console.log(res.data)
            this.results = res.data

      })
    },
    GoToSearch(){
        this.$router.push({ name: 'search' , params: { name: this.username, password: this.password}})
    },
    GoToPlaylists(){
        this.$router.push({ name: 'playlists' , params: { name: this.username, password: this.password}})
    },
    query(input){
        
        this.audio.pause()
        this.resI = input[0]["title"]
        this.SongThatsPLaying = this.resI
        this.test = input[0]
        console.log("sasd")
        const path = "http://127.0.0.1:5000/search/" + this.resI
        axios.get(path)
        .then(res => {
        console.log(res.data.url)
        this.audio = new Audio(res.data.url)
        this.audio.play()
        this.status = "pause"
      })
    },
    pause(){
        this.num += 1
        if(this.num % 2 == 0) {
            this.audio.pause()
            console.log(this.status)
            this.status = "resume"
        }
        else {
            this.audio.play()
            console.log(this.status)
            this.status = "pause"
        }

    },
    add_playlist(name){
        let title = name[0]["title"]
        this.$router.push({ name: 'addtoPlaylist' , params: { name: this.username, password: this.password, title: title}})
    }
    }

}
</script>

<template>  
      <div class="sidenav" >
        <h1 id = "title">Mezmur</h1>
        <a @click="GoToSearch()">search</a>
        <a @click="GoToPlaylists()">playists</a>
        <a href="#">Songs</a>
        <a href="#">artists</a>
        </div>
        <div>
            <input id = "search_input" type="text" v-model = "input"><button id = "button" @click="queryList">search</button>
        </div>
        <div v-for="x in results" id = "results">
            <a id = "titles" @click="query(x)">{{x[0]["title"]}}</a> <a id = "authors">{{x[0]["author"]}}</a>  <a v-if="test == x[0]" id = "playing">playing</a> <button id = "add_to_playlist" @click="add_playlist(x)">add to playlist</button>
        </div>
        <div v-if = "SongThatsPLaying" id = "now_playing">
          now playing
          <div id = "titlePlaying">{{SongThatsPLaying}}</div>
          <div @click = "pause()" id = "pause">{{status}}</div>
        </div>
</template>

<style>
#now_playing{
  font-size: 200%;
  color: #111;
  position: absolute;
  top: 90%;
  background-color: #f1f1f1;
  width: 80%;
  height: 10%;
  left: 15%;
}
#add_to_playlist{
    position: absolute;
    left: 90%;
    font-size: 110%;
    width: 10%;
}
#add_to_playlist:hover{
    background-color: rgb(173, 173, 173);
}
body{
    background-color: black;
}
#pause{
    bottom: 30%;
    position: absolute;
    left: 85%;
    font-size: 150%;
}
#playing{
    position: absolute;
    left: 85%;
    font-size: 150%;
}
#pause:hover{
    background-color: rgb(173, 173, 173);
}
#results{
    justify-content: space-between;
}
body{
    color: white;
}
#authors{
    color: rgb(155, 155, 155);
    position:absolute;
    font-size: 150%;
    left: 70%;
}
#titles{
    font-size: 150%;
    position: relative;
    left: 15%;
    margin-bottom: 10%;
}
#titles:hover{
    background-color: rgb(173, 173, 173);
}
#search_input{
    top: 20%;
    border-radius: 20px;
    position: relative;
    left: 25%;
    width: 55%;
}

#button{
    position: relative;
    left: 25%;

}

body{
    color: white;
}
#add{
        border: 1px solid white;
        padding-left: 10%;
        padding-right: 10%;
        color: white;
        position: absolute;
        left: 40%;
    }
    #add:hover{
        background-color: rgb(134, 134, 134);
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
