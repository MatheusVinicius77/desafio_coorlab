<template>

    <div class="search-container">
        <p class="text-2">Estas são as melhores alternativas de viagem para a data selecionada</p>
        <div class="search__result">
            <TripsBoxVue/>
        </div>
        <div class="search__result">
            <TripsBoxVue/>
        </div>

        <button class="bg-dark-orange clean-search-btn">Limpar</button>

    </div>

</template>

<script>
    import TripsBoxVue from '@/components/TripsBox.vue'
    export default{
    name: "SearchView",
    components: { 
        TripsBoxVue,
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
}
</script>

<style>

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


    @media (max-width: 790px) {
        .search-container{
            width: 100%;            
        }

        .clean-search-btn{
            margin-inline: auto;
            margin: 0;
        }

        .search__result{
            margin-top: 2rem;
        }

    }
</style>