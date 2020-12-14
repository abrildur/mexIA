const styleOptions = {
    backgroundColor: 'rgba(0, 0, 0, 0.8)',
    //bubbleBackground: '#FDA552',
    bubbleBackground: '#EE8421',
    bubbleBorderColor: '#EE8421',
    bubbleBorderRadius: 20,
    bubbleFromUserBackground: '#7C2D73',
    bubbleFromUserBorderColor: '#7C2D73',
    bubbleFromUserBorderRadius: 20,
    bubbleFromUserTextColor : '#FFFFFF',
    bubbleTextColor: "#FFFFFF",
    hideUploadButton: true,
    sendBoxBackground: '#1C1919',
    sendBoxButtonColor: '#FFFFFF',
    sendBoxButtonColorOnDisabled: '#CCC',
    sendBoxButtonColorOnFocus: '#F9A233',
    sendBoxButtonColorOnHover: '#F9A233',
    sendBoxTextColor: '#FFFFFF',
    sendBoxBorderBottom: 30,
    sendBoxBorderLeft: 30,
    sendBoxBorderRight: 30,
    rootHeight: '37rem',
    rootWidth: '55rem'
 }

 window.WebChat.renderWebChat(
    {
       directLine: window.WebChat.createDirectLine({
        secret: 'bXJYgAFXucg.Jmy08sOP0k_7XIs28JwGFxX7sfOuk6M-NJE0fxEeMxI'
       }),

       styleOptions
    },
    document.getElementById('webchat')
 );
 