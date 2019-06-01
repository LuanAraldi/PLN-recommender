<template>
  <div>
    <h1>Olá, obrigado por me ajudar na validação do meu TCC, basta seleciona qual vitrine abaixo você mais gosta</h1>
    <h2>O primeiro produto da vitrine é o produto referencia, os outros são recomendações</h2>
    <carousel :perPage=this.carousel.perPage>
      <slide>
        <selection option='A'></selection>
      </slide>
      <slide v-bind:key="rec.id" v-for="rec in recsA">
        <product 
          :img=rec.image
          :name=rec.name
          :price=rec.price>
        </product>
      </slide>
    </carousel>
    <carousel :perPage=this.carousel.perPage>
      <slide>
        <selection option='B'></selection>
      </slide>
      <slide v-bind:key="rec.id" v-for="rec in recsB">
        <product 
          :img=rec.image
          :name=rec.name
          :price=rec.price>
        </product>
      </slide>
    </carousel>
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel';
import Product from './components/Product'
import Selection from './components/Select'

const axios = require('axios')

export default {
  components: {
    Carousel,
    Slide,
    Product,
    Selection
  },
  data() {
    return {
      recFor: 'B005PB2T0S',
      recsA: [],
      recsB: [],
      carousel: {
        perPage: 6
      }
    }
  },
  mounted () {
    axios
      .get(`https://radiant-springs-66987.herokuapp.com/rec/pln/${this.recFor}`)
      .then((response => {
        this.recsA = response.data.recs
      }))
    axios
      .get(`https://radiant-springs-66987.herokuapp.com/rec/original/${this.recFor}`)
      .then((response => {
        this.recsB = response.data.recs
      }))
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
