import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '../views/MainView.vue'
import MovieView from '../views/MovieView.vue'
import RecommendView from '../views/RecommendView.vue'
import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import MovieList from '@/components/MovieList.vue'
import GenreList from '@/components/GenreList.vue'
import LatestList from '@/components/LatestList.vue'
import PopularList from '@/components/PopularList.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: MainView
  },
  {
    path: '/movies',
    name: 'Movie',
    component: MovieView,
    children : [
      {path:'all',component:MovieList},
      {path:'genre',component:GenreList},
      {path:'latest',component:LatestList},
      {path:'popular',component:PopularList},

    ]
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: RecommendView
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
