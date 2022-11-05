<template>
    <v-main>
        <v-container fluid style="height: 89vh">
            <v-row class="mt-16" style="max-height: 20vh">
                <v-col md="3"></v-col>
                <v-col md="9" align="center" align-self="end" class="mb-2">
                    <h2> Projetos sociais próximos a você! </h2>
                </v-col>
            </v-row>
            <v-row align="center" style="height: 40vh">
                <v-col md=3 align="right" align-self="center">
                    <v-card flat style="width:20vw;height:60vh" color="#d8d5d5">
                        <v-card-title class="justify-center"> <p1 class="font-size: 32px mt-8 mb-4">
                            Pesquisar
                        </p1> </v-card-title>
                        <v-card-actions class="justify-center">
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
                                class="mx-8"
                                ></v-autocomplete>
                        </v-card-actions>
                        <v-card-actions class="justify-center">
                            <v-card-title>
                            <p1 class="font-size:32px mt-8">
                                Filtrar
                            </p1>
                            </v-card-title>
                        </v-card-actions>
                    </v-card>
                </v-col>
                <v-col md=9 align="center" align-self="center">
                <client-only>
                    <l-map :zoom=17 :center="center" style="height:650px;width:1200px" ref="map">
                        <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
                        <!-- <l-marker :lat-lng="marker"></l-marker> -->
                        <v-locate-control/>
                        <v-geo :options="geosearchOptions"> </v-geo>
                    </l-map>
                </client-only>
                </v-col>
            </v-row>
        </v-container>
    </v-main>
</template>

<script>
export default {
    name: 'MapaPage',
    layout: 'navbar',
    data() {
        return {
            center: [-23.163577783622486, -45.79421561363161],
            //marker: [-23.163577783622486, -45.79421561363161],
            geosearchOptions: { 
                provider: this.$osm,
                style: 'bar',
                showMarker: true, 
                showPopup: false, 
                autoClose: true,
                searchLabel: 'Entre seu endereço', 
                keepResult: true,
            },
        }
    },
}
</script>

<style scoped>
    @import "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css";
    @import "https://unpkg.com/leaflet-geosearch@2.6.0/assets/css/leaflet.css"
</style>
