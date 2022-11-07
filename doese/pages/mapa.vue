<template>
    <v-main>
        <v-container fluid style="height: 105vh">
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
                    <l-map :zoom=17 :center="center" style="height:500px;width:1000px">
                        <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
                        <l-marker v-for="marker in markers" :key="marker.id" :lat-lng="marker.position">
                            <l-icon
                                :icon-size="[35, 35]"
                                :icon-anchor="[7, 32]"
                                icon-url="http://maps.google.com/mapfiles/ms/icons/red-dot.png"
                            />
                        </l-marker>
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
import {LIcon} from "vue2-leaflet";

export default {
    components: {
        LIcon
    },
    name: 'MapaPage',
    layout: 'navbar',
    data() {
        return {
            center: [-23.163577783622486, -45.79421561363161],
            markers: [ { 
                id: 'm1',
                position: [-23.163577783622486, -45.79421561363161],
            },
            { 
                id: 'm2',
                position: [-23.2049833407414, -45.88961422765064],
            },
            {
                id: 'm3',
                position: [-23.184120292802007, -45.878003193484986],
            },
            {
                id: 'm4',
                position: [-23.177809003532257, -45.888391834444825],
            }],
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
    @import "https://unpkg.com/leaflet-geosearch@2.6.0/assets/css/leaflet.css";
</style>
