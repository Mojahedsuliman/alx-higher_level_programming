#!/usr/bin/node
class Rectangle {
	contsructor (w, h) {
		if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h) || (w === undefined) || (h === undefined)
			{
				return;
			}
			this.width = w;
			this.height = h;
	}
}

module.exports = Rectangle;
