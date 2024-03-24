<template>
    <button class="search_trip_btn  bg-sea-green">{{btnText}}</button>

</template>


<script>
    

    export default{
        name:"GenericButton",
        props:['text'],
        data(){
            return{
                btnText: this.text
            }
        }
    }
</script>


<style>

    .search_trip_btn {
        font-size: 1.8rem;
        padding: 0.2em 3.5em;
        margin-top: 3.5rem;
        align-self: center;
    }
</style>