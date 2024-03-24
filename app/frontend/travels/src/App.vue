
<template>
  <div class="page">
    <AppSidebarVue/>
    <router-view>
    </router-view>

  </div>
  
</template>


<script>
import AppSidebarVue from "./components/AppSidebar.vue";

export default {

  components: {
    AppSidebarVue
  }
}
</script>

<style>
  .page{
    display: flex;
    min-height: 100vh;
    overflow: hidden;
    position: absolute;
    width: 100%;
  }
</style>
