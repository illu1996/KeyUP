<template>
  <div>
    <div>
      <video class="bg-video" playsinline="playsinline" autoplay="autoplay" muted="muted" loop="loop">
        <source src="@/assets/bg.mp4" type="video/mp4" />
      </video>
      <div>
        <div class="overlay"></div>
        <div class="loginform">
          <!-- <h2>로그인</h2>
        <form @submit.prevent="login">
          <label for="username">ID </label>
          <input type="text" id="username" v-model="username"><br>
  
          <label for="password">PASSWORD </label>
          <input type="password" id="password" v-model="password"><br>
  
          <button>LOGIN</button>
        </form>
        <router-link :to="{ name: 'Signup' }">회원가입</router-link> -->
        </div>
      </div>
    </div>


    <div class="login-wrap">
      <div class="login-html">
        <input id="tab-1" type="radio" name="tab" class="sign-in" checked><label for="tab-1" class="tab">로그인</label>
        <input id="tab-2" type="radio" name="tab" class="sign-up"><label for="tab-2" class="tab">회원가입</label>
        <div class="login-form">
          <form @submit.prevent="login" class="sign-in-htm">
            <div class="group">
              <label for="user" class="label" >Username</label>
              <input id="user" type="text" class="input" v-model="username">
            </div>
            <div class="group">
              <label for="pass1" class="label">Password</label>
              <input id="pass1" type="password" class="input" data-type="password" v-model="password">
            </div>
            <div class="group">
              <input type="submit" class="button" value="로그인">
            </div>
            <div class="hr"></div>
            <div class="foot-lnk">
              <a href="#forgot">비밀번호 찾기</a>
            </div>
          </form>
          <form class="sign-up-htm" @submit.prevent="signup">
            <div class="group">
              <label for="user1" class="label">Username</label>
              <input id="user1" type="text" class="input" v-model="upusername">
            </div>
            <div class="group">
              <label for="pass2" class="label">Password</label>
              <input id="pass2" type="password" class="input" v-model="uppassword1" data-type="password">
            </div>
            <div class="group">
              <label for="pass3" class="label">Repeat Password</label>
              <input id="pass3" type="password" class="input" v-model="uppassword2" data-type="password">
            </div>
            <div class="group">
              <input type="submit" class="button" value="회원가입">
            </div>
            <div class="hr"></div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script scoped>
import axios from 'axios';

export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
      upusername : null,
      uppassword1 : null,
      uppassword2 : null,
      pimg : null,
    }
  },

  methods: {
    login() {
      const username = this.username
      const password = this.password

      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/about/${username}/profile/`
      })
      .then((res) => {
        this.pimg = res.data.profileimg    
        const pimg = this.pimg
        const nickname = res.data.nickname
        const introduce = res.data.introduce

        const payload = {
          username, password, pimg, nickname, introduce
        }
        this.$store.dispatch('login', payload)
      })
    },
    signup() {
        const username = this.upusername
        const password1 = this.uppassword1
        const password2 = this.uppassword2
  
        const payload = {
          username, password1, password2
        }
        console.log(payload)
        this.$store.dispatch('signup', payload)
      }
  },
}
</script>


<style scoped>
.video-container {
  position: relative;
}


video.bg-video {
  position: fixed;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  transform: translateX(-50%) translateY(-50%);
  z-index: -1;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 60%;
  height: 100%;
  background-color: black;
  opacity: 0.8;
  z-index: 1;
}

.loginform {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
}


/* 여기부터 로그인폼 */

.login-wrap {
  width: 100%;
  margin-left: 15%;
  margin-top: 2%;
  max-width: 525px;
  min-height: 670px;
  position: relative;
  box-shadow: 0 12px 15px 0 rgba(0, 0, 0, .24), 0 17px 50px 0 rgba(0, 0, 0, .19);
  z-index: 2;
}

.login-html {
  width: 100%;
  height: 100%;
  position: absolute;
  padding: 90px 70px 50px 70px;
  background: rgb(228, 228, 228);
}

.login-html .sign-in-htm,
.login-html .sign-up-htm {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  position: absolute;
  transform: rotateY(180deg);
  backface-visibility: hidden;
  transition: all .4s linear;
}

.login-html .sign-in,
.login-html .sign-up,
.login-form .group .check {
  display: none;
}

.login-html .tab,
.login-form .group .label,
.login-form .group .button {
  text-transform: uppercase;
}

.login-html .tab {
  font-size: 22px;
  margin-right: 15px;
  padding-bottom: 5px;
  margin: 0 15px 10px 0;
  display: inline-block;
  border-bottom: 2px solid transparent;
  color: black;
}

.login-html .sign-in:checked+.tab,
.login-html .sign-up:checked+.tab {
  color: black;
  border-color: #151c83;
}


.login-form {
  min-height: 345px;
  position: relative;
  perspective: 1000px;
  transform-style: preserve-3d;
}

.login-form .group {
  margin-bottom: 15px;
}

.login-form .group .label,
.login-form .group .input,
.login-form .group .button {
  width: 100%;
  color: #fff;
  display: block;
}

.login-form .group .input,
.login-form .group .button {
  border: 1px solid rgba(112, 112, 112, 0.19);
  padding: 15px 20px;
  border-radius: 25px;
  background: rgba(255, 255, 255, .1);
}

.login-form .group input[data-type="password"] {
  text-security: circle;
  -webkit-text-security: circle;
}

.login-form .group .input[type="text"],
.login-form .group .input[type="password"] {
  color: black !important;
}

.login-form .group .label {
  color: #aaa;
  font-size: 12px;
}

.login-form .group .button {
  background: #151c83;
  margin-top: 40px;
}

.login-form .group label .icon {
  width: 15px;
  height: 15px;
  border-radius: 2px;
  position: relative;
  display: inline-block;
  background: rgba(255, 255, 255, .1);
}

.login-form .group label .icon:before,
.login-form .group label .icon:after {
  content: '';
  width: 10px;
  height: 2px;
  background: #fff;
  position: absolute;
  transition: all .2s ease-in-out 0s;
}

input::placeholder{
  color: black;
}

.login-form .group label .icon:before {
  left: 3px;
  width: 5px;
  bottom: 6px;
  transform: scale(0) rotate(0);
}

.login-form .group label .icon:after {
  top: 6px;
  right: 0;
  transform: scale(0) rotate(0);
}

.login-form .group .check:checked+label {
  color: #fff;
}

.login-form .group .check:checked+label .icon {
  background: #1161ee;
}

.login-form .group .check:checked+label .icon:before {
  transform: scale(1) rotate(45deg);
}

.login-form .group .check:checked+label .icon:after {
  transform: scale(1) rotate(-45deg);
}

.login-html .sign-in:checked+.tab+.sign-up+.tab+.login-form .sign-in-htm {
  transform: rotate(0);
}

.login-html .sign-up:checked+.tab+.login-form .sign-up-htm {
  transform: rotate(0);
}

.hr {
  height: 2px;
  margin: 60px 0 50px 0;
  background: rgba(255, 255, 255, .2);
}

.foot-lnk {
  text-align: center;
}</style>