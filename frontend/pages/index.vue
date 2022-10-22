<template>
    <v-main>
      <v-container fluid style="height: 250vh" class="mx-16 my-12">
        <v-row justify="left" class="ml-14 mt-8">
          <v-col md="6" align="center">
            <div style="height: 5vh">
            <p> Encontre projetos sociais próximos a você!</p>
            </div>
            <v-autocomplete
              v-model="select"
              :loading="loading"
              :items="items"
              :search-input.sync="search"
              cache-items
              flat
              hide-no-data
              hide-details
              label="Digite seu endereço"
              filled
              class="ml-8"
            ></v-autocomplete>
          </v-col>
          <v-col>
            <v-btn rounded class="mx-6 my-15" style="min-width:14vh" color="#c6535f">
              <div style="color:#f4f4f4;font-size:13px"> Buscar </div> </v-btn> </v-col>
        </v-row>
        <v-row justify="left" class="mx-14 mt-12" style="height: 62vh">
          <v-col md="6" align="center">
            <h1 style="font-size: 56px"> Quem você quer <br>
            ajudar hoje? </h1>
            <p style="font-size: 32px" class="font-weight-light mt-4"> A Doe-se oferece uma nova<br>
            maneira de engajar nos<br>
            projetos sociais mais<br>
            próximos de você!</p>
          </v-col>
          <v-col md="1">
          </v-col>
          <v-col md="4" justify="center">
            <v-card flat style="max-width: 65vh" color="#f6e2e2" class="mt-4">
              <v-card-title class="justify-center"> <h1 class="font-size: 48px my-8">
                  Faça sua doação
              </h1> </v-card-title>
              <v-card-actions class="justify-center">
                <v-btn color="#c6535f" style="min-width: 16vh" class="mb-6">
                  <div style="font-size:13px;color:#f4f4f4">
                    Doação Única
                  </div>
                </v-btn>
              </v-card-actions>
              <v-card-actions class="justify-center">
                <v-btn color="#c6535f" style="min-width: 16vh" class="mb-6" @click="entrar">
                  <div style="font-size:13px;color:#f4f4f4">
                    Entrar
                  </div>
                </v-btn>
              </v-card-actions>
              <v-card-actions class="justify-center">
                  <v-btn color="#c6535f" style="min-width: 16vh" class="mb-10">
                  <div style="font-size:13px;color:#f4f4f4">
                    Cadastre - se
                  </div>
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-divider style="max-width: 92vw"> </v-divider>

        <v-row class="ma-10" style="height:75vh">
          <v-col md="4" class="ma-10 ml-16" align="left">
            <p style="font-size:48px"> Quem Somos </p>
          </v-col>
          <v-col md="1"> </v-col>
          <v-col align-self="center">
            <v-card style="max-width:41vw" height="51vh" color="#f4f4f4" elevation="4">
              <v-card-actions class="justify-center">
            <v-img
              max-height="55vh"
              max-width="40vw"
              src="https://images.unsplash.com/photo-1579208570378-8c970854bc23?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1222&q=80">
            </v-img>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-divider style="max-width: 92vw"> </v-divider>
      </v-container>
    </v-main>
</template>

<script>
export default {
  name: 'IndexPage',
  layout: 'navbar',
  methods: {
    entrar () {
      this.$router.push('./UserLogin')
    }
  }
}
</script>
