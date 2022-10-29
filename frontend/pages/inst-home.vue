<template>
  <v-container fluid class="my-16">
    <v-card>
      <v-img class="text aling-end" :src="image3" max-height="15vh">
        <h1 align="left" style="color:#F08080">XXXX</h1>
        <div align="center">
          <v-toolbar color="#d3d3d3" flat max-width="1000" min-width="500">
            <v-tabs
              background-color="#d3d3d3" max-height="30"
              v-model="opcoes_inst" fixed-tabs slider-color="#FF5757"
            >
              <v-tab v-for="opcao in opcoes" :key="opcao" style="color: #000">
                {{ opcao }}
              </v-tab>
            </v-tabs>
          </v-toolbar>
        </div>
      </v-img>
    </v-card>
    <v-tabs-items v-model="opcoes_inst">
      <v-tab-item id="custom-publicacoes">
        <v-row>
          <v-col>
            <v-card>aaaaaaa
            </v-card>
          </v-col>
        </v-row>
      </v-tab-item>
    </v-tabs-items>
  </v-container>
</template>

<script>
export default {
  name: 'inst-home',
  layout: 'navbar',
  data: function () {
    return {
      opcoes_inst: null,
      image3: require('../assets/imagem-3.jpg'),
      opcoes: ['publicações', 'dados cadastrais', 'nova ação', 'nova publicação', 'notificações', 'ajuda']
    }
  }
}
</script>

<style>
#custom-publicacoes {
  background-color: white !important
}
.center {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
</style>
