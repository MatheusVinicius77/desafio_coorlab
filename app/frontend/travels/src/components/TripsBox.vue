<template>
    <div class="trip__wrapper">
        <div class="trip__info">
            <div class="trip__img bg-sea-green">
                <span class="">
                    <img class="img-trip" src="@/assets/timer.png" alt="{{}}}">
                </span>
            </div>
            <div class="trip__values bg-soft-gray">
                <p class="text-3">TC TRASNPORTES</p>
                <p>Leito: 13 (convencional)</p>
                <p>Tempo Estimado: 6h</p>
            </div>
        </div>
        <div class="trip__price_wrapper bg-soft-gray">
            <p class="text-3 trip__price ">Preço:</p>
            <p>R$ 1.250,00</p>
        </div>
    </div>
</template>

<script>
    export default{
    name: "TripsBox",
    data(){
    },
    
}
</script>

<style scoped>
    .trip__wrapper{
        display: flex;
        gap: 2rem;
        margin: 1rem;
    }

   

    .trip__info{
        display: flex;
        width: 60%;
    }
    
    .trip__values{
        padding: 1.5rem 2rem 1.5rem 3rem;
        flex-basis: 100%;
        flex-shrink: 2;
        
    }
    .trip__img{
        display: flex;
        align-items: center;
        padding: 0 1.8rem;
        border-radius: calc(1.5rem/5);
    }

    .trip__img span{
        width: 100%;
        display: flex;
        justify-content: center;

    }


    .trip__price_wrapper{
        padding: 2rem 6rem 2rem 2rem;
        flex-basis: 30%;
        
    }

    .trip__price {
        margin-bottom: 1rem;
        white-space: nowrap;
    }
    .trip__price_wrapper p:nth-child(2){
        white-space: nowrap;
    }


    @media (max-width: 790px) {
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

    

    }

</style>