import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import studentsModule from "@/store/modules/students";


const store = createStore({
    modules: {
        students: studentsModule
    },
    plugins: [createPersistedState()]
});


export default store;