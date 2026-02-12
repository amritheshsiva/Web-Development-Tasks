import { useParams } from "react-router-dom";
import { useSelector } from "react-redux";

function ViewProduct() {
  const { id } = useParams();

  const product = useSelector(state =>
    state.products.items.find(p => p.id === id)
  );

  if (!product) return <h3>Product not found</h3>;

  return (
    <div>
      <h2>{product.name}</h2>
      <p>{product.description}</p>
      <p>Price: {product.price}</p>
      <p>Quantity: {product.quantity}</p>
    </div>
  );
}

export default ViewProduct;
