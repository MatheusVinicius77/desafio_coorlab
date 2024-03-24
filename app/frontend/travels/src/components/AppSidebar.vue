<template>
    <aside data-visible="false" class="bg-soft-black">
      <img id="logo" src="../assets/logo.png" alt="GB Company Logo">
      <button  v-on:click="handleClose" data-visible="true" class="close-sidebar-btn">
          <img src="@/assets/close.svg" alt="">
      </button>
      <nav class="nav-container">
          <ul class="nav-list">
              <li class="nav-item">
                  <span class="nav-item__span">
                      <img src="@/assets/cal1.png" alt="">                    
                  </span>
                  <a class="text-1" href="#">Calculadora de Viagem</a>
              </li>
          </ul>
      </nav>
    </aside>
</template>
  
  <script>
  export default {
    name: 'AppSidebar',
    props: {
    },
    methods:{
        handleClose(){
            const hamburguer_button = document.querySelector("#hamburger-btn");
            const sidebar = document.querySelector("aside")
            const closeSidebar = document.querySelector(".close-sidebar-btn")
            sidebar.setAttribute("data-visible", 'false')
            hamburguer_button.setAttribute("data-visible", 'true')
            closeSidebar.setAttribute("data-visible", 'false')

        },
    }
  }
  </script>


  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    nav{
        margin-top: 5rem;
    }

    .nav-item{
        display: flex;
        align-items: center;
        height: 6rem;
    }


    .nav-item__span img{
        width: 2.2rem;
        margin-right: 1.5rem;

    }

    .nav-item a{
        font-size: clamp(1rem, 1.5vw,3rem);
        white-space: nowrap;
    }

    #logo{
        width: max(80%, 13rem);
    }

    aside{
        position: relative;
        padding: 3rem;
        z-index: 999999;
        max-width: 25%;
    }
    .close-sidebar-btn{
        position: absolute;
        background-color: transparent;
        left: 85%;
        top: 3%;
        visibility: hidden;

    }

    aside[data-visible='true']{
        transform: translateX(0);
        transition: all 350ms ease-in;
    }

    @media (max-width: 1044px) {
        aside{
            position: fixed;
            top:0;
            bottom: 0;
            max-width: 38%;
            min-width: 28rem;
            transform: translateX(-200%);
            transition: all 350ms ease-in;
        }

        .close-sidebar-btn[data-visible="true"]{
            visibility: visible;
        }

        .nav-item a{
            font-size: clamp(1.5rem,8%,3rem);
        }

        .nav-item__span img{
            max-width: 2.8rem;
            margin-right: 1.5rem;
            
        }

        #logo{
            width: clamp(9rem,30%,19rem);
        }



    }
  </style>
  