
import { useContext, useState } from "react";
import api from "../api";
import { AuthContext } from "../context/AuthContext";

export default function Login() {
  const { login } = useContext(AuthContext);
  const [form, setForm] = useState({ username: "", password: "" });

  const submit = async e => {
    e.preventDefault();
    const res = await api.post("/api/auth/login", form);
    const payload = JSON.parse(atob(res.data.access_token.split(".")[1]));
    login(res.data.access_token, payload.role);
    alert("Logged in");
  };

  return (
    <form onSubmit={submit}>
      <h2>Login</h2>
      <input placeholder="Username" onChange={e=>setForm({...form,username:e.target.value})} />
      <input type="password" placeholder="Password" onChange={e=>setForm({...form,password:e.target.value})} />
      <button>Login</button>
    </form>
  );
}
