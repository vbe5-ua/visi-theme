class FizzBuzz {
	public static void main(String[] args) {
		for (int num = 1; num <= 100; num++) {
			String text = "";

			if (num % 3 == 0)
				text += "fizz";
			if (num % 5 == 0)
				text += "buzz";
			if (text.isEmpty())
				text = Integer.toString(num);
            
            System.out.println(text);
		}
	}
}

class b extends FizzBuzz
{
    void a() throws CloneNotSupportedException{
        super.clone();
        
    }
}

class FizzBuzzObjectOriented {
    public static class FizzBuzz {
        private int num;
        private boolean divBy3;
        private boolean divBy5;
        private String text = new String();

        public FizzBuzz(int n) {
            num = n;
            divBy3 = num % 3 == 0;
            divBy5 = num % 5 == 0;
            text = "";
        }

        public void setText() {
            if (!divBy3 && !divBy5) {
                text = String.valueOf(num);
            } else {
                if (divBy3)
                    text += "fizz";
                if (divBy5)
                    text += "buzz";
            }
        }

        public String getText() {
            if (text.isEmpty())
                this.setText();
            return text;
        }
    }

    public static void main(String[] args) {
        FizzBuzz fb;
        int i;

        for (i = 1; i <= 100; i++) {
            fb = new FizzBuzz(i);
            System.out.println(fb.getText());
        }
    }
} 