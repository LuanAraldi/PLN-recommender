<template>   
  <div class="card">
    <p>
      <button>Opção {{option}}</button>
    </p>
  </div>
</template>

<script>
export default {
  name: 'Select',
  props: {
    option: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card {
  max-width: 300px;
}

.price {
  color: grey;
  font-size: 22px;
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
