<template>
  <div class="card">
    <img :src=img alt="Denim Jeans" style="width:100%">
    <h1>{{name}}</h1>
    <p class="price">${{price}}</p>
</div>
</template>

<script>
export default {
  name: 'Product',
  props: {
    img: String,
    name: String,
    price: Number
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 200px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.price {
  color: grey;
  font-size: 22px;
}
</style>
