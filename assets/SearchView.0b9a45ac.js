import{a as h}from"./axios.2576361e.js";import{_ as y,o as n,c as l,a as t,w as _,v as g,F as p,r as v,b as r,t as u,d as c}from"./index.74dfc967.js";const w={data(){let a=this.$route.params.name,s=this.$route.params.password;return{username:a,password:s,input:"",results:"",resI:"",test:"",status:"pause",audio:new Audio,num:1,SongThatsPLaying:null}},mounted(){},methods:{queryList(){console.log("sasd");const a="http://127.0.0.1:5000/searchList/"+this.input;h.get(a).then(s=>{console.log(s.data),this.results=s.data})},GoToSearch(){this.$router.push({name:"search",params:{name:this.username,password:this.password}})},GoToPlaylists(){this.$router.push({name:"playlists",params:{name:this.username,password:this.password}})},query(a){this.audio.pause(),this.resI=a[0].title,this.SongThatsPLaying=this.resI,this.test=a[0],console.log("sasd");const s="http://127.0.0.1:5000/search/"+this.resI;h.get(s).then(d=>{console.log(d.data.url),this.audio=new Audio(d.data.url),this.audio.play(),this.status="pause"})},OnRepeat(){this.audio.onended=()=>{this.audio.pause(),this.audio.play(),console.log("success")}},pause(){this.num+=1,this.num%2==0?(this.audio.pause(),console.log(this.status),this.status="resume"):(this.audio.play(),console.log(this.status),this.status="pause")},add_playlist(a){let s=a[0].title;this.$router.push({name:"addtoPlaylist",params:{name:this.username,password:this.password,title:s}})}}},k={class:"sidenav"},f=t("h1",{id:"title"},"Mezmur",-1),C=t("a",{href:"#"},"Songs",-1),S=t("a",{href:"#"},"artists",-1),T={id:"results"},L=["onClick"],P={class:"authors"},V={key:0,id:"playing"},q=["onClick"],b={key:0,id:"now_playing"},x={id:"titlePlaying"};function G(a,s,d,I,o,i){return n(),l(p,null,[t("div",k,[f,t("a",{onClick:s[0]||(s[0]=e=>i.GoToSearch())},"search"),t("a",{onClick:s[1]||(s[1]=e=>i.GoToPlaylists())},"playists"),C,S]),t("div",null,[_(t("input",{id:"search_input",type:"text","onUpdate:modelValue":s[2]||(s[2]=e=>o.input=e)},null,512),[[g,o.input]]),t("button",{id:"button",onClick:s[3]||(s[3]=(...e)=>i.queryList&&i.queryList(...e))},"search")]),(n(!0),l(p,null,v(o.results,e=>(n(),l("div",T,[t("a",{class:"titles",onClick:m=>i.query(e)},u(e[0].title),9,L),r(),t("a",P,u(e[0].author),1),r(),o.test==e[0]?(n(),l("a",V,"playing")):c("",!0),r(),t("button",{class:"add_to_playlist",onClick:m=>i.add_playlist(e)},"add to playlist",8,q)]))),256)),o.SongThatsPLaying?(n(),l("div",b,[r(" now playing "),t("div",x,u(o.SongThatsPLaying),1),t("div",{id:"repeat",onClick:s[4]||(s[4]=e=>i.OnRepeat())},"repeat"),t("div",{onClick:s[5]||(s[5]=e=>i.pause()),id:"pause"},u(o.status),1)])):c("",!0)],64)}const A=y(w,[["render",G]]);export{A as default};