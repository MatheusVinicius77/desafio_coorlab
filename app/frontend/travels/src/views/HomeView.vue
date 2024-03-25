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
                </h2>\
                <div class="input_wrapper">
                  <label class="text-3" for="destiny">Destino:</label>
                  <select v-model="formData.destiny" id="destiny" name="destiny">
                    <option value="" selected>Seleciona o Destino</option>
                    <option v-for="destination in destinations" :key="destination.id"
                      :value="destination">{{
                      destination}}</option>
                  </select>
                </div>

                <div class="input_wrapper">
                  <label class="text-3" for="travel_date">Data</label>
                  <input  v-model="formData.travelDate" id="travel_date" name="travel_date" type="date">
                </div>
                <GenericButton :text="btnText" />
                <button v-if="comfortable_travel && economic_travel" v-on:click="handleInputs"
                  class="bg-dark-orange clean-search-btn2">Limpar</button>

              </form>

            </div>
            <div class="dinamic_page">
              <div v-if="comfortable_travel && economic_travel" class="search-container">
                <p class="text-2">Estas são as melhores alternativas de viagem para a data selecionada</p>
                <div class="search__result">
                  <div class="trip__wrapper">
                    <div class="trip__info">
                      <div class="trip__img bg-sea-green">
                        <span class="">
                          <img class="img-trip" src="@/assets/timer.png" alt="{{}}}">
                        </span>
                      </div>
                      <div class="trip__values bg-soft-gray">
                        <p class="text-3">{{comfortable_travel.name}}</p>
                        <p>Leito: {{ comfortable_travel.bed}} (Completo)</p>
                        <p>Tempo Estimado: {{ comfortable_travel.duration}}</p>
                      </div>
                    </div>
                    <div class="trip__price_wrapper bg-soft-gray">
                      <p class="text-3 trip__price ">Preço:</p>
                      <p>{{ comfortable_travel.price_confort}}</p>
                    </div>
                  </div>
                </div>

                <div class="search__result">
                  <div class="trip__wrapper">
                    <div class="trip__info">
                      <div class="trip__img bg-sea-green">
                        <span class="">
                          <img class="img-trip" src="@/assets/timer.png" alt="{{}}}">
                        </span>
                      </div>
                      <div class="trip__values bg-soft-gray">
                        <p class="text-3">{{ economic_travel.name }}</p>
                        <p>Poltrona: {{ economic_travel.bed }} (convencional)</p>
                        <p>Tempo Estimado: {{ economic_travel.duration }}</p>
                      </div>
                    </div>
                    <div class="trip__price_wrapper bg-soft-gray">
                      <p class="text-3 trip__price ">Preço:</p>
                      <p>{{ economic_travel.price_econ }}</p>
                    </div>
                  </div>
                </div>
                <button v-on:click="handleInputs" class="bg-dark-orange clean-search-btn">Limpar</button>
              </div>
              <NothingSelectedView v-else />
            </div>
          </div>
        </div>
      </div>
      <TheModal />
    </div>
  </TheLayout>
</template>

<script>
import TheLayout from "@/layout/TheLayout.vue";
import NothingSelectedView from "./NothingSelectedView/NothingSelectedView.vue";
import GenericButton from "@/components/GenericButton.vue";
import TheModal from "@/components/TheModal.vue";
// @ is an alias to /src

export default{
  name:"HomeView",
  components:{
    TheLayout,
    NothingSelectedView,
    GenericButton,
    TheModal
},
  data(){
    return{
      destinations:[],
      formData: {
        travelDate: '',
        destiny: ''
      },
      comfortable_travel: null,
      economic_travel:null,
      btnText:"Buscar"
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
        if (travelDate && destiny){
            this.fetchTrips(destiny,travelDate);
        }else{
            this.handleModal()
        }

      },

      async fetchTrips(destiny, travelDate){
          const PATH1 = `http://127.0.0.1:3000/transports/comfortable/${destiny}/${travelDate}`;
          const PATH2 = `http://127.0.0.1:3000/transports/economic/${destiny}/${travelDate}`;

          try {
              const [comfortable,economic] = await Promise.all([
                fetch(PATH1), fetch(PATH2),
                  ]);

              this.comfortable_travel =  await comfortable.json();
              this.economic_travel =  await economic.json();
          } catch (error) {
              console.error(error);
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
  
      },

      handleInputs(){
        this.comfortable_travel = null
        this.economic_travel = null
        this.formData.destiny = ''
        this.formData.travelDate = ''
      },


      handleModal(){
        const modal = document.querySelector(".modal-container")
        const modalBackDrop = document.querySelector(".modal-backdrop")

        if(modal.getAttribute('data-visible') == 'True'){
          modal.setAttribute('data-visible','False')
          modalBackDrop.setAttribute('data-visible', 'False')

        }else{
          modal.setAttribute('data-visible', 'True')
          modalBackDrop.setAttribute('data-visible', 'True')

        }
        console.log(modal, modalBackDrop)
      }


  }
    }
</script>


<style scoped>


 .trip__wrapper {
   display: flex;
   gap: 2rem;
   margin-bottom: 1rem;
 }



 .trip__info {
   display: flex;
   width: 60%;
 }

 .trip__values {
   padding: 1.5rem 2rem 1.5rem 3rem;
   flex-basis: 100%;
   flex-shrink: 2;

 }

 .trip__img {
   display: flex;
   align-items: center;
   padding: 0 1.8rem;
   border-radius: calc(1.5rem/5);
 }

 .trip__img span {
   width: 100%;
   display: flex;
   justify-content: center;

 }


 .trip__price_wrapper {
   padding: 2rem 6rem 2rem 2rem;
   flex-basis: 30%;

 }

 .trip__price {
   margin-bottom: 1rem;
   white-space: nowrap;
 }

 .trip__price_wrapper p:nth-child(2) {
   white-space: nowrap;
 }

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
        gap: 2rem;
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

    .input_wrapper label{
        margin-bottom: 0.4rem;
    }

    .input_wrapper{
        margin-top: 2rem;
        width: 100%;        
    }

    .view__container{
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
    }


    #hamburger-btn{
        position: relative;
        margin-left: 3rem;
        bottom: 2%;
        visibility: hidden;

    }

    .search-container{
      display: flex;
      flex-direction: column;
      height: 100%;
      padding-bottom: 1rem;
      margin-left: 2rem;
  }
  .clean-search-btn{
      font-size: 1.5rem;
      padding: 0.5rem 6rem;
      border-radius: 0.4rem;
      align-self: flex-end;
      margin-top: auto;        
  }

    .clean-search-btn2{
        display: none;
    }

  @media (max-width: 790px) {
        .search-container{
            width: 100%;
            margin-left: 0;
        }

        .main__container{
            row-gap: 1rem;
        }

        .clean-search-btn{
            margin-inline: auto;
            margin: 0;
        }

        .search__result{
            margin-top: 2rem;
        }


        .trip__wrapper{
            flex-direction: column;
            gap: 0;
        }

        .trip__info{
            width: 100%;
            flex-wrap: wrap;
        }

        .trip__img{
            width: 100%;
        }
  .trip__wrapper{
            flex-direction: column;
            gap: 0;
        }

        .trip__info{
            width: 100%;
            flex-wrap: wrap;
        }

        .trip__img{
            width: 100%;
        }
        .trip__wrapper {
          flex-direction: column;
          gap: 0;
        }
  
        .trip__info {
          width: 100%;
          flex-wrap: wrap;
        }
  
        .trip__img {
          width: 100%;
        }

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

      @media (max-width: 790px) {
        .search-container{
            width: 100%;            
        }

        .clean-search-btn{
            margin-inline: auto;
            display: none;
        }

        .clean-search-btn2{
          display: block;
          margin-top: 1rem;
          align-self: center;
          font-size: 1.8rem;
            padding: 0.2em 3.5em;
        }

        .search__result{
            margin-top: 2rem;
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