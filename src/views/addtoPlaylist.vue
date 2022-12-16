<script>
import axios from 'axios';
export default {
    data(){
        return{

        }
    },
    mounted() {
        axios.get("http://127.0.0.1:5000/searchList/")
    },
}
</script>
<template>
    <div v-for = "x in ">
        
    </div>
</template>

<script>

</script>

