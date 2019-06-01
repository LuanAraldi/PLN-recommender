<template>   
  <div class="card">
    <p>
      <button v-on:click="sendEvent()">Opção {{option}}</button>
    </p>
  </div>
</template>

<script>
const axios = require('axios')

export default {
  name: 'Select',
  props: {
    option: String
  },
  methods: {
    sendEvent: function () {
      const event = {
        'cookie': document.cookie, 
        'option': this.$options.propsData.option
      }

      axios.post('https://radiant-springs-66987.herokuapp.com/event', event)
      .then(function () {
        alert('Muito Obrigado!')
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card {
  max-width: 300px;
}

.card button {
  border: none;
  outline: 0;
  padding: 12px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

.card button:hover {
  opacity: 0.7;
}

button {
  margin-top: 30%;
}
</style>
