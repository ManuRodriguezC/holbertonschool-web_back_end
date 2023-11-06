-- Create trigger that decreases the quantity items.
CREATE TRIGGER decrease_items AFTER INSERT ON orders FOR EACH Row
    UPDATE items SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name
;