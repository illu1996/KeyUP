import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '../views/MainView.vue'
import MovieView from '../views/MovieView.vue'
import RecommendView from '../views/RecommendView.vue'
import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import CommunityView from '../views/CommunityView.vue'
import SearchView from '../views/SearchView.vue'

import MovieList from '@/components/MovieList.vue'
import GenreList from '@/components/GenreList.vue'
import LatestList from '@/components/LatestList.vue'
import PopularList from '@/components/PopularList.vue'
import MovieDetail from '@/views/MovieDetail.vue'
import ArticleCreate from '@/components/ArticleCreate.vue'
import ArticleList from '@/components/ArticleList.vue'
import ArticleDetail from '@/components/ArticleDetail.vue'
import ProfileDetail from '@/components/ProfileDetail.vue'
import ProfileUpdate from '@/components/ProfileUpdate.vue'

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
    component: ProfileView,
    children : [
      {path:'detail/:username',component:ProfileDetail},
      {path:'update',component:ProfileUpdate},
    ]
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
  {
    path: '/moviedetail',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView,
    children : [
      {path:'create',component:ArticleCreate},
      {path:'list',component:ArticleList},
    ]
  },
  {
    path: '/article/:id',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
