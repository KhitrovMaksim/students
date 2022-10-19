import {createRouter, createWebHistory} from "vue-router";

import NotFound from "@/pages/NotFound";
import StudentsList from "@/pages/students/StudentsList";
import StudentManaging from "@/pages/students/StudentManaging";
import StudentAdd from "@/pages/students/StudentAdd";


const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', redirect: '/students'  },
        { path: '/students', component: StudentsList },
        { path: '/students/:id', component: StudentManaging, props: true },
        { path: '/add', component: StudentAdd },
        { path: '/:notFound(.*)', component: NotFound }
    ]
});


export default router;