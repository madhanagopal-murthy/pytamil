grammar மாத்திரை;

// start: மாத்திரை ;

மாத்திரை : ஒர்_எழுத்து_ஒரு_மொழி
            | ஈர்_எழுத்து_ஒரு_மொழி
            | பொதுமொழி;
            

// இரண்டு மாத்திரைக்கு மிகாத சொல்
ஒர்_எழுத்து_ஒரு_மொழி : ஒரெழுத்து;

// இரண்டு மாத்திரைக்கு மிகாத சொல்
ஈர்_எழுத்து_ஒரு_மொழி : ஈர்_மொழிமுதல் ஈர்_மொழியிறுதி;

// இரண்டு மாத்திரையின் மிக்கு ஒலிக்கும் சொல்
பொதுமொழி : மொழிமுதல் மொழியிடை*? மொழியிறுதி;

ஒரெழுத்து : உயிரளபெடை | உயிர்மெய்க்குறில் | உயிர்மெய்நெடில் | உயிர்க்குறில் | உயிர்நெடில்;

ஈர்_மொழிமுதல் : உயிரளபெடை | உயிர்மெய்க்குறில் | உயிர்க்குறில் ;

ஈர்_மொழியிறுதி : உயிரளபெடை | உயிர்மெய்க்குறில்;

மொழிமுதல் :  ஔகாரக்குறுக்கம் | ஐகாரக்குறுக்கம்_முதல் | உயிரளபெடை
                | உயிர்மெய்க்குறில் | உயிர்மெய்நெடில் | உயிர்க்குறில் | உயிர்நெடில் | மெய்;

மொழியிடை :  ஆய்தக்குறுக்கம் | குற்றியலிகரம்_புணர்மொழி | ஐகாரக்குறுக்கம்_இடைகடை 
                | மகரக்குறுக்கம்_புணர்மொழி | உயிரளபெடை | ஒற்றளபெடை 
                | உயிர்மெய்க்குறில் | உயிர்மெய்நெடில் |  மெய் | ஆய்தம் ;

மொழியிறுதி : உயிரளபெடை | குற்றியலிகரம்_தனிமொழி 
                | மகரக்குறுக்கம்_தனிமொழி | ஐகாரக்குறுக்கம்_இடைகடை | குற்றியலுகரம் 
                | உயிர்மெய்நெடில் | உயிர்மெய்க்குறில் | மெய்  ; 

குறிலிணை : உயிர்க்குறில் உயிர்மெய்க்குறில்
            | உயிர்மெய்க்குறில் உயிர்மெய்க்குறில் ;

// அளபெடை
உயிரளபெடை: மெய் உயிரளபெடை_எழுத்து | உயிரளபெடை_எழுத்து;
ஒற்றளபெடை: ஒற்றளபெடை_எழுத்து ஒற்றளபெடை_எழுத்து ;


// குறுக்கம்
குற்றியலுகரம்: வல்லினம் 'உ'; // 0.5
ஐகாரக்குறுக்கம்_முதல் : 'ஐ' ; //1.5
ஐகாரக்குறுக்கம்_இடைகடை:  மெய் 'ஐ' ; // 1
ஔகாரக்குறுக்கம்: 'ஔ' | மெய் 'ஔ'; // 1
ஆய்தக்குறுக்கம் : 'ஃற்இ' | 'ஃட்ஈ';  // ஃறி ஃடீ
குற்றியலிகரம்_தனிமொழி : 'ம்இய்ஆ' ; // மியா எனும் அசைச்சொல்
குற்றியலிகரம்_புணர்மொழி : வல்லினம் 'இ' 'ய்' உயிர்க்குறில் 
                            | வல்லினம் 'இ' 'ய்' உயிர்நெடில் ;
மகரக்குறுக்கம்_தனிமொழி : 'ண்' 'ம்' | 'ன்' 'ம்';
மகரக்குறுக்கம்_புணர்மொழி : 'ம்வ்அ' ; // ம்வ

// # சார்பு எழுத்து

உயிர்மெய்க்குறில் : மெய் உயிர்க்குறில் ;
உயிர்மெய்நெடில் : மெய் உயிர்நெடில்;

உயிர்க்குறில் :'அ'|'இ'|'உ'|'எ'|'ஒ' ;
உயிர்நெடில் :  'ஆ'|'ஈ'|'ஊ'|'ஏ'|'ஐ'|'ஓ'|'ஔ';
ஆய்தம் : 'ஃ'; 
மெய் : 'க்'|'ச்'|'ட்'|'த்'|'ப்'|'ற்'|'ஞ்'|'ங்'|'ண்'
        |'ந்'|'ம்'|'ன்'|'ய்'|'ர்'|'ல்'|'வ்'|'ழ்'|'ள்' ;

வல்லினம்:  'க்'|'ச்'|'ட்'|'த்'|'ப்'|'ற்';
        
உயிரளபெடை_எழுத்து : 'ஆஅ'| 'ஈஇ'|'ஊஉ'| 'ஏஎ'| 'ஐஇ'| 'ஓஒ'| 'ஔஉ' ;
 
ஒற்றளபெடை_எழுத்து : 'ங்' | 'ஞ்' | 'ண்' | 'ந்' | 'ம்' | 'ய்'
                        | 'ல்' | 'வ்' | 'ள்' | 'ன்' | 'ஃ' ;


// ஐகாரக்குறுக்கம் : 1 #ஐகு
// ஔகாரக்குறுக்கம் : 1  #ஔகு
// குற்றியலுகரம் : 0.5  #குற்றியலுகரம்
// குற்றியலிகரம் : 0.5  #குலி
// மகரக்குறுக்கம் : 0.25 #மகு
// ஆய்தக்குறுக்கம் : 0.25  #ஆகு