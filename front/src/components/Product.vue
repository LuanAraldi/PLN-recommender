<template>
  <div class="card">
    <img :src=img alt="Denim Jeans" style="width:100%">
    <h3>{{name}}</h3>
    <p class="price">${{price}}</p>
</div>
</template>

<script>
export default {
  name: 'Product',
  props: {
    img: String,
    name: String,
    price: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
img {
  max-height: 1000px;
}

.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 200px;
  max-height: 500px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.price {
  color: grey;
  font-size: 14px;
}
</style>
