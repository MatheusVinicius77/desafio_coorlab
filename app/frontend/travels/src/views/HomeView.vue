<template>
  <TheLayout>
    <div class="homepage__container">
      <button v-on:click="handleHamburguer" data-visible="true" id="hamburger-btn">
          <img src="@/assets/black-hamburger.png" alt="">
      </button>
      <hr>
      <div class="homepage__div bg-soft-gray">
          <div class="homepage__content_wrapper">
              <header class="bg-soft-black">
                  <h2 class="text-1">
                      <span><img src="@/assets/truck.png" alt=""></span>
                      Calculadora de Viagem
                  </h2>
              </header>
              <div class="main__container bg-white">
                  <div class="trip_calculator bg-soft-gray">
                      <form @submit.prevent="handleSubmit">
                          <h2 class="form__title text-2">
                              <span><img src="@/assets/trust.png" alt="Palm giving an heart"></span>
                              Calcule o Valor da Viagem
                          </h2>
                          <div class="input_wrapper">
                              <label class="text-3" for="destiny">Destino:</label>
                              <select  v-model="formData.destiny" id="destiny" name="destiny" >
                                  <option  value="" selected>Seleciona o Destino</option>
                                  <option v-for="destination in destinations" :key="destination.id" :value="destination">{{ destination}}</option>   
                              </select>
                          </div>

                          <div class="input_wrapper">
                              <label class="text-3" for="travel_date">Data</label>
                              <input v-model="formData.travelDate" id="travel_date" name="travel_date" type="date">
                          </div>
                          <button  class="search_trip_btn  bg-sea-green">Buscar</button>
                      
                      </form>
                  </div>
                  <div class="dinamic_page">
                      <SearchView :test="msg"/>
                  </div>
              </div>
          </div>
      </div>
    </div>
  </TheLayout>
</template>

<script>
import TheLayout from "@/layout/TheLayout.vue";
import SearchView from "./SearchView/SearchView.vue";
// @ is an alias to /src

export default{
  name:"HomeView",
  components:{
    TheLayout,
    SearchView
},
  data(){
    return{
      destinations:[],
      formData: {
        travelDate: '',
        destiny: ''
      },
    }
  },
  mounted() {
      this.fetchDestinations();
  },
  methods: {
      async fetchDestinations() {
          
          const PATH = `http://localhost:3000/cities/`
          console.log(PATH)
          try {
              const response = await fetch(PATH);
              if (!response.ok) {
                  throw new Error('Erro ao buscar usuários');
              }
              const data = await response.json();
              this.destinations = data;
          } catch (error) {
              console.error('Erro ao buscar usuários:', error);
          }
      },

      handleSubmit(){
          const travelDate = this.formData['travelDate']
          const destiny = this.formData['destiny']
          
          this.fetchTrips(destiny,travelDate);

      },

      async fetchTrips(destiny, travelDate){
          const PATH = `http://127.0.0.1:3000/transports/comfortable/${destiny}/${travelDate}`;

          try {
              const [fastest] = await Promise.all([
                  fetch(PATH),
                  ]);

              this.msg = await fastest.json();
          } catch (error) {
              console.error(error, 'eae');
          }

      },

      handleHamburguer(){
          const hamburguer_button = document.querySelector("#hamburger-btn");
          const sidebar = document.querySelector("aside")
          const closeSidebar = document.querySelector(".close-sidebar-btn")
          sidebar.setAttribute("data-visible", 'true')
          hamburguer_button.setAttribute("data-visible", 'false')
          closeSidebar.setAttribute("data-visible", 'true')
          console.log(sidebar)
  
      }


  }
    }
</script>


<style scoped>


    hr{
        height: 0.15rem;
        border: none;
        background-color: rgba(0, 0, 0, 0.312);
        box-shadow: 0px 1px 5px 0.5px rgba(32, 30, 30, 0.689);
        
    }

    .homepage__container{
        padding-top: 7rem;
        flex-basis: 100%;
        height: 100%;

    }


    .homepage__div{
        padding-inline: 3rem;
        padding-top: 5vh;
        height: 100%;
        flex-basis: 100%;        
    }

    .homepage__content_wrapper{
        max-width: 100rem;
        margin: 0 auto;
    }


    header{
        padding: 0.5rem 2rem;
        border-radius: 0.3rem;
    }

    header h2{
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .main__container{
        display: flex;
        padding: 3rem 2rem 2rem 2rem;
        box-shadow: 3px 2px 2px white;
    }
   
    .trip_calculator{
        flex-basis: 35%;
        border-radius: 0.5rem;
        padding-inline: 1.5rem;
        padding-block: 3rem 9rem;
        
    }

    .dinamic_page{
      width: 70%;
    }

    form{
        display: flex;;
        flex-direction: column;
    }

    .form__title{
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .form__title span img{
        width: 3rem;
    }

    .input_wrapper input, .input_wrapper select{
        padding: 0.2rem;
        height: 3rem;
        width: 100%;
    }


    .search_trip_btn{
        font-size: 1.8rem;
        padding: 0.2em 3.5em;
        margin-top: 3.5rem;
        align-self: center;
    }

    .input_wrapper label{
        margin-bottom: 0.4rem;
    }

    .input_wrapper{
        margin-top: 2rem;
        width: 100%;        
    }

    .view__container{
        width: 100%;
    }


    #hamburger-btn{
        position: relative;
        margin-left: 3rem;
        bottom: 2%;
        visibility: hidden;
    }

 
    @media (max-width: 1044px) {

        .trip_calculator{
            height: fit-content;
        }
        
        #hamburger-btn{
            visibility:visible;
        }


        #hamburger-btn[data-visible="false"]{
            visibility: hidden;
        }


      }


      @media (max-width: 520px) {
        .main__container{
            flex-wrap: wrap;
            gap: 0;
        }

        .trip_calculator{
            flex-basis: 100%;
            margin-bottom: 9rem;
        }

        .dinamic_page{
            flex-basis: 100%;
        }
    


      }

</style>