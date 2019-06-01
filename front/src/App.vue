<template>
  <div>
    <carousel :perPage=this.carousel.perPage>
      <slide>
        <selection option='A'></selection>
      </slide>
      <slide>
        <product 
          img='https://images-na.ssl-images-amazon.com/images/I/41iQlt6ZBLL._AC_SY240_.jpg'
          name='Controle Xbox One'
          price=25>
        </product>
      </slide>
      <slide>
        <product img='https://images-na.ssl-images-amazon.com/images/I/41iQlt6ZBLL._AC_SY240_.jpg'></product>
      </slide>
      <slide>
        <product img='https://images-na.ssl-images-amazon.com/images/I/41iQlt6ZBLL._AC_SY240_.jpg'></product>
      </slide>
      <slide>
        <product img='https://images-na.ssl-images-amazon.com/images/I/41iQlt6ZBLL._AC_SY240_.jpg'></product>
      </slide>
    </carousel>
    <carousel :perPage=this.carousel.perPage>
      <slide>
        <selection option='B'></selection>
      </slide>
      <slide>
        <product 
          img='https://images-na.ssl-images-amazon.com/images/I/41iQlt6ZBLL._AC_SY240_.jpg'
          name='Controle Xbox One'
          price=25>
        </product>
      </slide>
      <slide>
        <product img='https://images-na.ssl-images-amazon.com/images/I/41iQlt6ZBLL._AC_SY240_.jpg'></product>
      </slide>
      <slide>
        <product img='https://images-na.ssl-images-amazon.com/images/I/41iQlt6ZBLL._AC_SY240_.jpg'></product>
      </slide>
      <slide>
        <product img='https://images-na.ssl-images-amazon.com/images/I/41iQlt6ZBLL._AC_SY240_.jpg'></product>
      </slide>
    </carousel>
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel';
import Product from './components/Product'
import Selection from './components/Select'

export default {
  components: {
    Carousel,
    Slide,
    Product,
    Selection
  },
  data() {
    return {
      carousel: {
        perPage: 5
      }
    }
  },
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
