
export default function SweetCard({ sweet, onPurchase, isAdmin, onDelete }) {
  return (
    <div className="card">
      <h3>{sweet.name}</h3>
      <p>{sweet.category}</p>
      <p>₹{sweet.price}</p>
      <p>Stock: {sweet.quantity}</p>

      <button disabled={sweet.quantity === 0} onClick={()=>onPurchase(sweet.id)}>
        Purchase
      </button>

      {isAdmin && <button onClick={()=>onDelete(sweet.id)}>Delete</button>}
    </div>
  );
}
