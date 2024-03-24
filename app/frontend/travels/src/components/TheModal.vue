<template>
    <div data-visible="False" class="modal-backdrop">
        <div class="modal-container">
            <img src="@/assets/exclamation.png" alt="Exclamation signal">
            <p>Insira os valores para realizar <br> a cotação</p>
            <GenericButton v-on:click="handleModal" :text="btnText" />
        </div>
    </div>
</template>

<script>
import GenericButton from "./GenericButton.vue"
export default {
    name: "TheModal",
    data() {
        return {
            btnText: "Fechar"
        };
    },

    methods:{
        handleModal(){
            const modal = document.querySelector(".modal-container")
            const modalBackDrop = document.querySelector(".modal-backdrop")

            if (modal.getAttribute('data-visible') == 'True') {
                modal.setAttribute('data-visible', 'False')
                modalBackDrop.setAttribute('data-visible', 'False')

            } else {
                modal.setAttribute('data-visible', 'True')
                modalBackDrop.setAttribute('data-visible', 'True')

            }
            console.log(modal, modalBackDrop)
        }
    },
    components: { GenericButton }
}
</script>


<style>

    .modal-backdrop{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 9999;
        display: none;
    }
    
    .modal-container{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: white;
        padding: 20px;
        z-index: 1000;
        display: none;
        text-align: center;
        /* Certifique-se de que o modal fique acima da sobreposição */
    }


    .modal-container[data-visible='False'] {
        display: none;
    }

    .modal-container[data-visible='True']{
        display: block;
    }

    .modal-backdrop[data-visible='False'] {
        display: none;
    }

    .modal-backdrop[data-visible='True'][data-visible='True']{
        display: block;
    }

</style>