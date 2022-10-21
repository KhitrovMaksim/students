import {createRouter, createWebHistory} from "vue-router";

import NotFound from "@/pages/NotFound";
import StudentsList from "@/pages/students/StudentsList";
import StudentAdd from "@/pages/students/StudentAdd";
import About from "@/pages/About";
import StudentView from "@/pages/students/StudentView";


const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', redirect: '/students'  },
        { path: '/about', component: About  },
        { path: '/students', component: StudentsList },
        { path: '/students/:id', component: StudentView, props: true },
        { path: '/add', component: StudentAdd },
        { path: '/:notFound(.*)', component: NotFound }
    ]
});


export default router;