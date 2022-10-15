import {createRouter, createWebHistory} from "vue-router";

import NotFound from "@/pages/NotFound";
import StudentsList from "@/pages/students/StudentsList";


const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', redirect: '/students'  },
        { path: '/students', component: StudentsList },
        { path: '/:notFound(.*)', component: NotFound }
    ]
});


export default router;