
import { AuthProvider } from "./context/AuthContext";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Admin from "./pages/Admin";
import { useState } from "react";

export default function App() {
  const [page, setPage] = useState("login");

  return (
    <AuthProvider>
      <nav>
        <button onClick={()=>setPage("login")}>Login</button>
        <button onClick={()=>setPage("register")}>Register</button>
        <button onClick={()=>setPage("dashboard")}>Dashboard</button>
        <button onClick={()=>setPage("admin")}>Admin</button>
      </nav>

      {page === "login" && <Login />}
      {page === "register" && <Register />}
      {page === "dashboard" && <Dashboard />}
      {page === "admin" && <Admin />}
    </AuthProvider>
  );
}
